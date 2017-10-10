"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import acel_lcm_msgs.Pose_t

import acel_lcm_msgs.Point3Df_t

import acel_lcm_msgs.QuadrotorTransform

class LaserScanPoints_t(object):
    __slots__ = ["trans_sensor2world", "point_num", "points", "pose"]

    def __init__(self):
        self.trans_sensor2world = acel_lcm_msgs.Pose_t()
        self.point_num = 0
        self.points = []
        self.pose = acel_lcm_msgs.QuadrotorTransform()

    def encode(self):
        buf = BytesIO()
        buf.write(LaserScanPoints_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        assert self.trans_sensor2world._get_packed_fingerprint() == acel_lcm_msgs.Pose_t._get_packed_fingerprint()
        self.trans_sensor2world._encode_one(buf)
        buf.write(struct.pack(">q", self.point_num))
        for i0 in range(self.point_num):
            assert self.points[i0]._get_packed_fingerprint() == acel_lcm_msgs.Point3Df_t._get_packed_fingerprint()
            self.points[i0]._encode_one(buf)
        assert self.pose._get_packed_fingerprint() == acel_lcm_msgs.QuadrotorTransform._get_packed_fingerprint()
        self.pose._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != LaserScanPoints_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return LaserScanPoints_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = LaserScanPoints_t()
        self.trans_sensor2world = acel_lcm_msgs.Pose_t._decode_one(buf)
        self.point_num = struct.unpack(">q", buf.read(8))[0]
        self.points = []
        for i0 in range(self.point_num):
            self.points.append(acel_lcm_msgs.Point3Df_t._decode_one(buf))
        self.pose = acel_lcm_msgs.QuadrotorTransform._decode_one(buf)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if LaserScanPoints_t in parents: return 0
        newparents = parents + [LaserScanPoints_t]
        tmphash = (0x41cb5b1499974f70+ acel_lcm_msgs.Pose_t._get_hash_recursive(newparents)+ acel_lcm_msgs.Point3Df_t._get_hash_recursive(newparents)+ acel_lcm_msgs.QuadrotorTransform._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if LaserScanPoints_t._packed_fingerprint is None:
            LaserScanPoints_t._packed_fingerprint = struct.pack(">Q", LaserScanPoints_t._get_hash_recursive([]))
        return LaserScanPoints_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

