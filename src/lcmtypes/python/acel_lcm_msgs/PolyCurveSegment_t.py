"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class PolyCurveSegment_t(object):
    __slots__ = ["coeffsize_x", "coeffsize_y", "coeffsize_z", "coeffsize_yaw", "coeffs_x", "coeffs_y", "coeffs_z", "coeffs_yaw", "t_start", "t_end"]

    def __init__(self):
        self.coeffsize_x = 0
        self.coeffsize_y = 0
        self.coeffsize_z = 0
        self.coeffsize_yaw = 0
        self.coeffs_x = []
        self.coeffs_y = []
        self.coeffs_z = []
        self.coeffs_yaw = []
        self.t_start = 0.0
        self.t_end = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(PolyCurveSegment_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">iiii", self.coeffsize_x, self.coeffsize_y, self.coeffsize_z, self.coeffsize_yaw))
        buf.write(struct.pack('>%dd' % self.coeffsize_x, *self.coeffs_x[:self.coeffsize_x]))
        buf.write(struct.pack('>%dd' % self.coeffsize_y, *self.coeffs_y[:self.coeffsize_y]))
        buf.write(struct.pack('>%dd' % self.coeffsize_z, *self.coeffs_z[:self.coeffsize_z]))
        buf.write(struct.pack('>%dd' % self.coeffsize_yaw, *self.coeffs_yaw[:self.coeffsize_yaw]))
        buf.write(struct.pack(">dd", self.t_start, self.t_end))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != PolyCurveSegment_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return PolyCurveSegment_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = PolyCurveSegment_t()
        self.coeffsize_x, self.coeffsize_y, self.coeffsize_z, self.coeffsize_yaw = struct.unpack(">iiii", buf.read(16))
        self.coeffs_x = struct.unpack('>%dd' % self.coeffsize_x, buf.read(self.coeffsize_x * 8))
        self.coeffs_y = struct.unpack('>%dd' % self.coeffsize_y, buf.read(self.coeffsize_y * 8))
        self.coeffs_z = struct.unpack('>%dd' % self.coeffsize_z, buf.read(self.coeffsize_z * 8))
        self.coeffs_yaw = struct.unpack('>%dd' % self.coeffsize_yaw, buf.read(self.coeffsize_yaw * 8))
        self.t_start, self.t_end = struct.unpack(">dd", buf.read(16))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if PolyCurveSegment_t in parents: return 0
        tmphash = (0xfd820417caf41e97) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if PolyCurveSegment_t._packed_fingerprint is None:
            PolyCurveSegment_t._packed_fingerprint = struct.pack(">Q", PolyCurveSegment_t._get_hash_recursive([]))
        return PolyCurveSegment_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

