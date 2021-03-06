module Poly1305
#set-options "--z3rlimit 20 --max_fuel 0"
open Spec.Lib.IntTypes
open Spec.Lib.RawIntTypes
open Spec.Lib.IntSeq
open Speclib
let blocksize = 0x10 
let block_t = bytes_t 0x10 
let key_t = bytes_t 0x20 
let tag_t = bytes_t 0x10 
let subblock = x:vlbytes{(length x <= 0x10)} 
let subblock_t = subblock 
let p130m5 = nat ((0x2 **. 0x82) -. 0x5) 
let felem = x:nat{(x < p130m5)} 
let felem_t = felem 
let to_felem (x:nat_t) : felem_t =
  felem (nat (x %. p130m5)) 
let fadd (x:felem_t) (y:felem_t) : felem_t =
  to_felem (x +. y) 
let fmul (x:felem_t) (y:felem_t) : felem_t =
  to_felem (nat (x *. y)) 
let encode (block:subblock_t) : felem_t =
  let b = create 0x10 (u8 0x0) in 
  let b = update_slice b 0x0 (length block) block in 
  let welem = to_felem (uint128.to_nat (uint_from_bytes_le #U128 b)) in 
  let lelem = to_felem (nat (0x2 **. (0x8 *. (length block)))) in 
  fadd lelem welem 
let encode_r (r:block_t) : felem_t =
  let ruint = uint_from_bytes_le #U128 r in 
  let ruint = (ruint &. u128 0xffffffc0ffffffc0ffffffc0fffffff) in 
  let r_nat = uint128.to_nat ruint in 
  to_felem r_nat 
let poly (text:vlbytes_t) (r:felem_t) : felem_t =
  let (blocks,last) = split_blocks text blocksize in 
  let acc = felem (nat 0x0) in 
  let acc = repeati (range (length blocks))
    (fun i acc ->
      let acc = fmul (fadd acc (encode (subblock blocks.[i]))) r in 
      acc)
    acc in 
  let acc = if ((length last > 0x0)) then (let acc = fmul (fadd acc (encode (subblock (bytes last)))) r in acc )else (acc) in 
  acc 
let poly1305_mac (text:vlbytes_t) (k:key_t) : tag_t =
  let r = slice k 0x0 blocksize in 
  let s = slice k blocksize (0x2 *. blocksize) in 
  let relem = encode_r r in 
  let selem = uint_from_bytes_le #U128 s in 
  let a = poly text relem in 
  let n = u128 ((u128 a) +. selem) in 
  tag_t (uint_to_bytes_le #U128 n) 
