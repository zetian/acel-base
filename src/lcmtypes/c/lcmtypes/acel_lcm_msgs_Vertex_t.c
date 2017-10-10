// THIS IS AN AUTOMATICALLY GENERATED FILE.  DO NOT MODIFY
// BY HAND!!
//
// Generated by lcm-gen

#include <string.h>
#include "lcmtypes/acel_lcm_msgs_Vertex_t.h"

static int __acel_lcm_msgs_Vertex_t_hash_computed;
static uint64_t __acel_lcm_msgs_Vertex_t_hash;

uint64_t __acel_lcm_msgs_Vertex_t_hash_recursive(const __lcm_hash_ptr *p)
{
    const __lcm_hash_ptr *fp;
    for (fp = p; fp != NULL; fp = fp->parent)
        if (fp->v == __acel_lcm_msgs_Vertex_t_get_hash)
            return 0;

    __lcm_hash_ptr cp;
    cp.parent =  p;
    cp.v = (void*)__acel_lcm_msgs_Vertex_t_get_hash;
    (void) cp;

    uint64_t hash = (uint64_t)0xebb7afb0e54cf3b4LL
         + __int64_t_hash_recursive(&cp)
         + __float_hash_recursive(&cp)
        ;

    return (hash<<1) + ((hash>>63)&1);
}

int64_t __acel_lcm_msgs_Vertex_t_get_hash(void)
{
    if (!__acel_lcm_msgs_Vertex_t_hash_computed) {
        __acel_lcm_msgs_Vertex_t_hash = (int64_t)__acel_lcm_msgs_Vertex_t_hash_recursive(NULL);
        __acel_lcm_msgs_Vertex_t_hash_computed = 1;
    }

    return __acel_lcm_msgs_Vertex_t_hash;
}

int __acel_lcm_msgs_Vertex_t_encode_array(void *buf, int offset, int maxlen, const acel_lcm_msgs_Vertex_t *p, int elements)
{
    int pos = 0, element;
    int thislen;

    for (element = 0; element < elements; element++) {

        thislen = __int64_t_encode_array(buf, offset + pos, maxlen - pos, &(p[element].id), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_encode_array(buf, offset + pos, maxlen - pos, p[element].position, 3);
        if (thislen < 0) return thislen; else pos += thislen;

    }
    return pos;
}

int acel_lcm_msgs_Vertex_t_encode(void *buf, int offset, int maxlen, const acel_lcm_msgs_Vertex_t *p)
{
    int pos = 0, thislen;
    int64_t hash = __acel_lcm_msgs_Vertex_t_get_hash();

    thislen = __int64_t_encode_array(buf, offset + pos, maxlen - pos, &hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    thislen = __acel_lcm_msgs_Vertex_t_encode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

int __acel_lcm_msgs_Vertex_t_encoded_array_size(const acel_lcm_msgs_Vertex_t *p, int elements)
{
    int size = 0, element;
    for (element = 0; element < elements; element++) {

        size += __int64_t_encoded_array_size(&(p[element].id), 1);

        size += __float_encoded_array_size(p[element].position, 3);

    }
    return size;
}

int acel_lcm_msgs_Vertex_t_encoded_size(const acel_lcm_msgs_Vertex_t *p)
{
    return 8 + __acel_lcm_msgs_Vertex_t_encoded_array_size(p, 1);
}

int __acel_lcm_msgs_Vertex_t_decode_array(const void *buf, int offset, int maxlen, acel_lcm_msgs_Vertex_t *p, int elements)
{
    int pos = 0, thislen, element;

    for (element = 0; element < elements; element++) {

        thislen = __int64_t_decode_array(buf, offset + pos, maxlen - pos, &(p[element].id), 1);
        if (thislen < 0) return thislen; else pos += thislen;

        thislen = __float_decode_array(buf, offset + pos, maxlen - pos, p[element].position, 3);
        if (thislen < 0) return thislen; else pos += thislen;

    }
    return pos;
}

int __acel_lcm_msgs_Vertex_t_decode_array_cleanup(acel_lcm_msgs_Vertex_t *p, int elements)
{
    int element;
    for (element = 0; element < elements; element++) {

        __int64_t_decode_array_cleanup(&(p[element].id), 1);

        __float_decode_array_cleanup(p[element].position, 3);

    }
    return 0;
}

int acel_lcm_msgs_Vertex_t_decode(const void *buf, int offset, int maxlen, acel_lcm_msgs_Vertex_t *p)
{
    int pos = 0, thislen;
    int64_t hash = __acel_lcm_msgs_Vertex_t_get_hash();

    int64_t this_hash;
    thislen = __int64_t_decode_array(buf, offset + pos, maxlen - pos, &this_hash, 1);
    if (thislen < 0) return thislen; else pos += thislen;
    if (this_hash != hash) return -1;

    thislen = __acel_lcm_msgs_Vertex_t_decode_array(buf, offset + pos, maxlen - pos, p, 1);
    if (thislen < 0) return thislen; else pos += thislen;

    return pos;
}

int acel_lcm_msgs_Vertex_t_decode_cleanup(acel_lcm_msgs_Vertex_t *p)
{
    return __acel_lcm_msgs_Vertex_t_decode_array_cleanup(p, 1);
}

int __acel_lcm_msgs_Vertex_t_clone_array(const acel_lcm_msgs_Vertex_t *p, acel_lcm_msgs_Vertex_t *q, int elements)
{
    int element;
    for (element = 0; element < elements; element++) {

        __int64_t_clone_array(&(p[element].id), &(q[element].id), 1);

        __float_clone_array(p[element].position, q[element].position, 3);

    }
    return 0;
}

acel_lcm_msgs_Vertex_t *acel_lcm_msgs_Vertex_t_copy(const acel_lcm_msgs_Vertex_t *p)
{
    acel_lcm_msgs_Vertex_t *q = (acel_lcm_msgs_Vertex_t*) malloc(sizeof(acel_lcm_msgs_Vertex_t));
    __acel_lcm_msgs_Vertex_t_clone_array(p, q, 1);
    return q;
}

void acel_lcm_msgs_Vertex_t_destroy(acel_lcm_msgs_Vertex_t *p)
{
    __acel_lcm_msgs_Vertex_t_decode_array_cleanup(p, 1);
    free(p);
}

int acel_lcm_msgs_Vertex_t_publish(lcm_t *lc, const char *channel, const acel_lcm_msgs_Vertex_t *p)
{
      int max_data_size = acel_lcm_msgs_Vertex_t_encoded_size (p);
      uint8_t *buf = (uint8_t*) malloc (max_data_size);
      if (!buf) return -1;
      int data_size = acel_lcm_msgs_Vertex_t_encode (buf, 0, max_data_size, p);
      if (data_size < 0) {
          free (buf);
          return data_size;
      }
      int status = lcm_publish (lc, channel, buf, data_size);
      free (buf);
      return status;
}

struct _acel_lcm_msgs_Vertex_t_subscription_t {
    acel_lcm_msgs_Vertex_t_handler_t user_handler;
    void *userdata;
    lcm_subscription_t *lc_h;
};
static
void acel_lcm_msgs_Vertex_t_handler_stub (const lcm_recv_buf_t *rbuf,
                            const char *channel, void *userdata)
{
    int status;
    acel_lcm_msgs_Vertex_t p;
    memset(&p, 0, sizeof(acel_lcm_msgs_Vertex_t));
    status = acel_lcm_msgs_Vertex_t_decode (rbuf->data, 0, rbuf->data_size, &p);
    if (status < 0) {
        fprintf (stderr, "error %d decoding acel_lcm_msgs_Vertex_t!!!\n", status);
        return;
    }

    acel_lcm_msgs_Vertex_t_subscription_t *h = (acel_lcm_msgs_Vertex_t_subscription_t*) userdata;
    h->user_handler (rbuf, channel, &p, h->userdata);

    acel_lcm_msgs_Vertex_t_decode_cleanup (&p);
}

acel_lcm_msgs_Vertex_t_subscription_t* acel_lcm_msgs_Vertex_t_subscribe (lcm_t *lcm,
                    const char *channel,
                    acel_lcm_msgs_Vertex_t_handler_t f, void *userdata)
{
    acel_lcm_msgs_Vertex_t_subscription_t *n = (acel_lcm_msgs_Vertex_t_subscription_t*)
                       malloc(sizeof(acel_lcm_msgs_Vertex_t_subscription_t));
    n->user_handler = f;
    n->userdata = userdata;
    n->lc_h = lcm_subscribe (lcm, channel,
                                 acel_lcm_msgs_Vertex_t_handler_stub, n);
    if (n->lc_h == NULL) {
        fprintf (stderr,"couldn't reg acel_lcm_msgs_Vertex_t LCM handler!\n");
        free (n);
        return NULL;
    }
    return n;
}

int acel_lcm_msgs_Vertex_t_subscription_set_queue_capacity (acel_lcm_msgs_Vertex_t_subscription_t* subs,
                              int num_messages)
{
    return lcm_subscription_set_queue_capacity (subs->lc_h, num_messages);
}

int acel_lcm_msgs_Vertex_t_unsubscribe(lcm_t *lcm, acel_lcm_msgs_Vertex_t_subscription_t* hid)
{
    int status = lcm_unsubscribe (lcm, hid->lc_h);
    if (0 != status) {
        fprintf(stderr,
           "couldn't unsubscribe acel_lcm_msgs_Vertex_t_handler %p!\n", hid);
        return -1;
    }
    free (hid);
    return 0;
}

