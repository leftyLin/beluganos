// -*- coding: utf-8 -*-

// Copyright (C) 2019 Nippon Telegraph and Telephone Corporation.
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

package templates

import (
	"io"
	"text/template"
)

const playbookInventory = `
[hosts]
localhost

[{{ .Name }}-hosts]
{{- range .Hosts }}
{{ . }}
{{- end }}
`

func NewPlaybookInventoryTemplate() *template.Template {
	return template.Must(template.New("inventory").Parse(playbookInventory))
}

type PlaybookInventory struct {
	Name  string
	Hosts []string
}

func NewPlaybookInventory() *PlaybookInventory {
	return &PlaybookInventory{
		Hosts: []string{},
	}
}

func (p *PlaybookInventory) AddHost(host string) {
	p.Hosts = append(p.Hosts, host)
}

func (p *PlaybookInventory) AddHosts(hosts ...string) {
	for _, host := range hosts {
		p.AddHost(host)
	}
}

func (p *PlaybookInventory) Execute(w io.Writer) error {
	return NewPlaybookInventoryTemplate().Execute(w, p)
}
