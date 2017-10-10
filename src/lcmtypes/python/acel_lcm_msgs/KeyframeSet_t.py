"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import acel_lcm_msgs.TimeStamp_t

import acel_lcm_msgs.Keyframe_t

class KeyframeSet_t(object):
    __slots__ = ["kf_num", "kfs", "sys_time", "path_id"]

    def __init__(self):
        self.kf_num = 0
        self.kfs = []
        self.sys_time = acel_lcm_msgs.TimeStamp_t()
        self.path_id = 0

    def encode(self):
        buf = BytesIO()
        buf.write(KeyframeSet_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.kf_num))
        for i0 in range(self.kf_num):
            assert self.kfs[i0]._get_packed_fingerprint() == acel_lcm_msgs.Keyframe_t._get_packed_fingerprint()
            self.kfs[i0]._encode_one(buf)
        assert self.sys_time._get_packed_fingerprint() == acel_lcm_msgs.TimeStamp_t._get_packed_fingerprint()
        self.sys_time._encode_one(buf)
        buf.write(struct.pack(">q", self.path_id))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != KeyframeSet_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return KeyframeSet_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = KeyframeSet_t()
        self.kf_num = struct.unpack(">q", buf.read(8))[0]
        self.kfs = []
        for i0 in range(self.kf_num):
            self.kfs.append(acel_lcm_msgs.Keyframe_t._decode_one(buf))
        self.sys_time = acel_lcm_msgs.TimeStamp_t._decode_one(buf)
        self.path_id = struct.unpack(">q", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if KeyframeSet_t in parents: return 0
        newparents = parents + [KeyframeSet_t]
        tmphash = (0x7e244a5374dace1f+ acel_lcm_msgs.Keyframe_t._get_hash_recursive(newparents)+ acel_lcm_msgs.TimeStamp_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if KeyframeSet_t._packed_fingerprint is None:
            KeyframeSet_t._packed_fingerprint = struct.pack(">Q", KeyframeSet_t._get_hash_recursive([]))
        return KeyframeSet_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

