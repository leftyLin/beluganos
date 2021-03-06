// -*- coding: utf-8 -*-
// +build gobgpv2

// Copyright (C) 2018 Nippon Telegraph and Telephone Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
// implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package gobgputil

import (
	"context"
	"fmt"
	"gonla/nlalib"
	"io"

	api "github.com/osrg/gobgp/api"
	log "github.com/sirupsen/logrus"
	"google.golang.org/grpc"
)

var (
	FamilyIPv4UC = &api.Family{
		Afi:  api.Family_AFI_IP,
		Safi: api.Family_SAFI_UNICAST,
	}
	FamilyIPv6UC = &api.Family{
		Afi:  api.Family_AFI_IP6,
		Safi: api.Family_SAFI_UNICAST,
	}
)

var family_values = map[string]*api.Family{
	"ipv4-unicast": FamilyIPv4UC,
	"ipv6-unicast": FamilyIPv6UC,
}

func parseRouteFamily(s string) (*api.Family, error) {
	if v, ok := family_values[s]; ok {
		return v, nil
	}
	return nil, fmt.Errorf("invalid route family. %s", s)
}

type BgpMonitor struct {
	client api.GobgpApiClient
	conn   *grpc.ClientConn
	connCh chan *nlalib.ConnInfo
	family *api.Family
}

func NewBgpMonitor(addr string, routeFamily string) (*BgpMonitor, error) {
	family, err := parseRouteFamily(routeFamily)
	if err != nil {
		return nil, err
	}

	connCh := make(chan *nlalib.ConnInfo)
	conn, err := nlalib.NewClientConn(addr, connCh)
	if err != nil {
		close(connCh)
		return nil, err
	}

	return &BgpMonitor{
		client: api.NewGobgpApiClient(conn),
		conn:   conn,
		connCh: connCh,
		family: family,
	}, nil
}

func (s *BgpMonitor) Serve(done <-chan struct{}, cb func(*api.Path)) {

	log.Infof("Serve: Started")

	pathCh := make(chan *api.Path)
	defer close(pathCh)

	for {
		select {
		case <-s.connCh:
			log.Infof("Serve: connected.")
			go s.MonitorTable(pathCh)

		case path := <-pathCh:
			log.Debugf("Serve: %v", path)
			cb(path)

		case <-done:
			log.Infof("Serve: Exit")
			return
		}
	}
}

func (s *BgpMonitor) MonitorTable(ch chan<- *api.Path) {
	log.Infof("MonitorTable Start.")

	req := &api.MonitorTableRequest{
		Type:    api.Resource_GLOBAL,
		Family:  FamilyIPv4UC,
		Current: true,
	}

	stream, err := s.client.MonitorTable(context.Background(), req)
	if err != nil {
		log.Errorf("MonitorTable error. %s", err)
		return
	}

	for {
		res, err := stream.Recv()
		if err == io.EOF {
			log.Infof("MonitorRib Recv end. %s", err)
			break
		}
		if err != nil {
			log.Errorf("MonitorRib error. %s", err)
			break
		}

		ch <- res.Path
	}

	log.Infof("MonitorRib Exit.")
}
