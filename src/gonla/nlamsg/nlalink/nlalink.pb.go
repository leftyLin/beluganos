// Code generated by protoc-gen-go. DO NOT EDIT.
// source: nlalink.proto

package nlalink

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Node struct {
	Ip                   []byte   `protobuf:"bytes,1,opt,name=ip,proto3" json:"ip,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Node) Reset()         { *m = Node{} }
func (m *Node) String() string { return proto.CompactTextString(m) }
func (*Node) ProtoMessage()    {}
func (*Node) Descriptor() ([]byte, []int) {
	return fileDescriptor_b86348b8158a5a04, []int{0}
}

func (m *Node) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Node.Unmarshal(m, b)
}
func (m *Node) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Node.Marshal(b, m, deterministic)
}
func (m *Node) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Node.Merge(m, src)
}
func (m *Node) XXX_Size() int {
	return xxx_messageInfo_Node.Size(m)
}
func (m *Node) XXX_DiscardUnknown() {
	xxx_messageInfo_Node.DiscardUnknown(m)
}

var xxx_messageInfo_Node proto.InternalMessageInfo

func (m *Node) GetIp() []byte {
	if m != nil {
		return m.Ip
	}
	return nil
}

type Vpn struct {
	Ip                   []byte   `protobuf:"bytes,1,opt,name=ip,proto3" json:"ip,omitempty"`
	Mask                 []byte   `protobuf:"bytes,2,opt,name=mask,proto3" json:"mask,omitempty"`
	Gw                   []byte   `protobuf:"bytes,3,opt,name=gw,proto3" json:"gw,omitempty"`
	Label                uint32   `protobuf:"varint,4,opt,name=label,proto3" json:"label,omitempty"`
	VpnGw                []byte   `protobuf:"bytes,5,opt,name=vpn_gw,json=vpnGw,proto3" json:"vpn_gw,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Vpn) Reset()         { *m = Vpn{} }
func (m *Vpn) String() string { return proto.CompactTextString(m) }
func (*Vpn) ProtoMessage()    {}
func (*Vpn) Descriptor() ([]byte, []int) {
	return fileDescriptor_b86348b8158a5a04, []int{1}
}

func (m *Vpn) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Vpn.Unmarshal(m, b)
}
func (m *Vpn) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Vpn.Marshal(b, m, deterministic)
}
func (m *Vpn) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Vpn.Merge(m, src)
}
func (m *Vpn) XXX_Size() int {
	return xxx_messageInfo_Vpn.Size(m)
}
func (m *Vpn) XXX_DiscardUnknown() {
	xxx_messageInfo_Vpn.DiscardUnknown(m)
}

var xxx_messageInfo_Vpn proto.InternalMessageInfo

func (m *Vpn) GetIp() []byte {
	if m != nil {
		return m.Ip
	}
	return nil
}

func (m *Vpn) GetMask() []byte {
	if m != nil {
		return m.Mask
	}
	return nil
}

func (m *Vpn) GetGw() []byte {
	if m != nil {
		return m.Gw
	}
	return nil
}

func (m *Vpn) GetLabel() uint32 {
	if m != nil {
		return m.Label
	}
	return 0
}

func (m *Vpn) GetVpnGw() []byte {
	if m != nil {
		return m.VpnGw
	}
	return nil
}

func init() {
	proto.RegisterType((*Node)(nil), "nlalink.Node")
	proto.RegisterType((*Vpn)(nil), "nlalink.Vpn")
}

func init() { proto.RegisterFile("nlalink.proto", fileDescriptor_b86348b8158a5a04) }

var fileDescriptor_b86348b8158a5a04 = []byte{
	// 142 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0xcd, 0xcb, 0x49, 0xcc,
	0xc9, 0xcc, 0xcb, 0xd6, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x62, 0x87, 0x72, 0x95, 0xc4, 0xb8,
	0x58, 0xfc, 0xf2, 0x53, 0x52, 0x85, 0xf8, 0xb8, 0x98, 0x32, 0x0b, 0x24, 0x18, 0x15, 0x18, 0x35,
	0x78, 0x82, 0x98, 0x32, 0x0b, 0x94, 0xd2, 0xb8, 0x98, 0xc3, 0x0a, 0xf2, 0xd0, 0x85, 0x85, 0x84,
	0xb8, 0x58, 0x72, 0x13, 0x8b, 0xb3, 0x25, 0x98, 0xc0, 0x22, 0x60, 0x36, 0x48, 0x4d, 0x7a, 0xb9,
	0x04, 0x33, 0x44, 0x4d, 0x7a, 0xb9, 0x90, 0x08, 0x17, 0x6b, 0x4e, 0x62, 0x52, 0x6a, 0x8e, 0x04,
	0x8b, 0x02, 0xa3, 0x06, 0x6f, 0x10, 0x84, 0x23, 0x24, 0xca, 0xc5, 0x56, 0x56, 0x90, 0x17, 0x9f,
	0x5e, 0x2e, 0xc1, 0x0a, 0x56, 0xc9, 0x5a, 0x56, 0x90, 0xe7, 0x5e, 0x9e, 0xc4, 0x06, 0x76, 0x8f,
	0x31, 0x20, 0x00, 0x00, 0xff, 0xff, 0xb6, 0x8c, 0x86, 0x48, 0xa0, 0x00, 0x00, 0x00,
}
