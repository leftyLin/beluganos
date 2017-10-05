// -*- coding: utf-8 -*-

// Copyright (C) 2017 Nippon Telegraph and Telephone Corporation.
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

package ribsyn

import (
	"fmt"
	"github.com/osrg/gobgp/table"
	log "github.com/sirupsen/logrus"
	"golang.org/x/net/context"
	"gonla/nlaapi"
	"gonla/nlalib"
	"gonla/nlamsg"
	"gonla/nlamsg/nlalink"
	"net"
)

type NLAController struct {
	client nlaapi.NLAApiClient
	connCh chan *nlalib.ConnInfo
	nlaCh  chan *nlamsg.NetlinkMessageUnion
}

func NewNLAController() *NLAController {
	return &NLAController{
		client: nil,
		connCh: make(chan *nlalib.ConnInfo),
		nlaCh:  make(chan *nlamsg.NetlinkMessageUnion),
	}
}

func (n *NLAController) Conn() <-chan *nlalib.ConnInfo {
	return n.connCh
}

func (n *NLAController) Recv() <-chan *nlamsg.NetlinkMessageUnion {
	return n.nlaCh
}

func (n *NLAController) Start(addr string) error {
	conn, err := nlalib.NewClientConn(addr, n.connCh)
	if err != nil {
		return err
	}

	n.client = nlaapi.NewNLAApiClient(conn)
	return nil
}

func (n *NLAController) GetRoutes(f func(*nlamsg.Route)) error {
	stream, err := n.client.GetRoutes(context.Background(), &nlaapi.GetRoutesRequest{})
	if err != nil {
		return err
	}
	for {
		route, err := stream.Recv()

		if err != nil {
			break
		}

		f(route.ToNative())
	}
	return nil
}

func (n *NLAController) Monitor() error {
	stream, err := n.client.MonNetlink(context.Background(), &nlaapi.MonNetlinkRequest{})
	if err != nil {
		return err
	}

	log.Infof("NLAC Monitor:")

	go func() {
		for {
			nlmsg, err := stream.Recv()
			if err != nil {
				log.Infof("NLAC Monitor: EXIT. %s", err)
				break
			}

			n.nlaCh <- nlmsg.ToNative()
		}
	}()

	return nil
}

func (n *NLAController) AddVpn(nid uint8, path *table.Path, labels []uint32, vpnGw net.IP) error {
	if len(labels) != 1 {
		return fmt.Errorf("NLAC AddVpn: Invalid Label List. %v", labels)
	}

	_, prefix, err := net.ParseCIDR(path.GetNlri().String())
	if err != nil {
		return err
	}

	gw := path.GetNexthop()
	req := &nlaapi.ModVpnRequest{
		Type: nlalink.RTM_NEWVPN,
		Vpn:  nlaapi.NewVpn(nid, prefix, gw, labels[0], vpnGw),
	}

	_, err = n.client.ModVpn(context.Background(), req)
	return err
}

func (n *NLAController) DelVpn(nid uint8, dst *net.IPNet) error {
	req := &nlaapi.ModVpnRequest{
		Type: nlalink.RTM_DELVPN,
		Vpn:  nlaapi.NewVpn(nid, dst, net.IP{}, 0, nil),
	}
	_, err := n.client.ModVpn(context.Background(), req)
	return err
}
