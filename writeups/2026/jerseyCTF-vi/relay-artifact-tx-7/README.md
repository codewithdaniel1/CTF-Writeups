# Relay Artifact TX-7

**JerseyCTF VI · 2026**

A diagnostic value shares a prime factor with an RSA modulus. One greatest common divisor turns the public key material into the private key needed to read the relay.

[View the styled writeup on my website](https://codewithdaniel1.github.io/writeups/2026/jerseyCTF-vi/relay-artifact-tx-7/relay-artifact-tx-7.html)

## The challenge

Relay node TX-7 was recovered from a decommissioned corridor between the outer and inner system. Diagnostics show it prepared a final transmission but never sent it - the relay restrained itself. Reconstruct what TX-7 was trying to say; its last unsent message may point toward the only viable route inward.

- [Original challenge archive](assets/original/03-relay-artifact-tx-7.zip)

## Recover the private key

Let `n` be the RSA modulus and `diagnostic` the supplied value. Their greatest common divisor exposes one prime. The other factor follows by division:

```
from math import gcd

p = gcd(n, diagnostic)
assert 1 < p < n
q = n // p
```

With both primes, compute Euler’s totient and invert the public exponent `e` to obtain the private exponent `d`:

```
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
```

This is the standard RSA key relation. The supplied integers are used directly; the calculation does not search the key space.

## Decrypt the relay

Convert the ciphertext bytes to an integer, apply RSA decryption, then convert the result back to bytes. The modulus size determines the fixed-width block. It begins with PKCS#1 v1.5 encryption padding (`00 02`), so read the message after the next zero-byte separator:

```
ciphertext_int = int.from_bytes(ciphertext, "big")
message_int = pow(ciphertext_int, d, n)
block_size = (n.bit_length() + 7) // 8
block = message_int.to_bytes(block_size, "big")
assert block.startswith(b"\x00\x02")
plaintext = block[2:].split(b"\x00", 1)[1]
print(plaintext.decode())
```

The plaintext reads:

**Relay Transmission — UNSENT**

The restraint was not ordered.
It was negotiated.

Direct control provokes resistance.
Indirect action is tolerated.

Partial restoration maintained system stability.

Do not restore everything.

The message ends with the flag:

```
JCTF{INDIRECT_CONTROL_IS_THE_ONLY_CONTROL}
```

- [Recovered relay transmission](assets/recovered/relay-artifact-tx-7-transmission.txt)

- [Recovered flag file](assets/recovered/relay-artifact-tx-7-flag.txt)

## Takeaway

RSA depends on keeping the prime factors of `n` secret. If another published value leaks a factor, the private exponent can be reconstructed and textbook RSA decryption becomes possible. A quick GCD check can therefore reveal a critical key-generation failure.
