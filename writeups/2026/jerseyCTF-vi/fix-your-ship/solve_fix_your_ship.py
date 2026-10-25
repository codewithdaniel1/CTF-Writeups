#!/usr/bin/env python3
"""Reconstruct the corrupted JerseyCTF VI 'Fix Your Ship' challenge files.

Usage:
    python3 solve_fix_your_ship.py path/to/file1 path/to/file2 path/to/file3

The script verifies the observed corruption before changing any bytes. It does
not change the originals, and it does not rely on pre-encoded flag text.
"""
from pathlib import Path
import argparse


def write_repaired(src: Path, target: Path, before: bytes, after: bytes,
                   start: int, ending: bool = False) -> None:
    contents = bytearray(src.read_bytes())
    offset = len(contents) - len(before) if ending else start
    observed = bytes(contents[offset:offset + len(before)])
    if observed != before:
        raise ValueError(
            f"{src}: expected {before.hex(' ')} at byte offset {offset:#x}; "
            f"found {observed.hex(' ')}"
        )
    contents[offset:offset + len(before)] = after
    target.write_bytes(contents)
    print(f"{src.name}: 0x{offset:06x}: {before.hex(' ')} -> {after.hex(' ')}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file1', type=Path)
    parser.add_argument('file2', type=Path)
    parser.add_argument('file3', type=Path)
    parser.add_argument('--out', type=Path, default=Path('repaired'))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    # PNG: the 89 50 4E 47 0D 0A 1A 0A signature lost 'PNG'.
    write_repaired(args.file1, args.out/'file1.png', b'\x00\x00\x00',
                   b'PNG', 1)

    # JPEG: repair SOI/APP0 prefix, then EOI marker at end of file.
    jpeg_out = args.out/'file2.jpg'
    write_repaired(args.file2, jpeg_out, b'\x00\x00\x00',
                   bytes.fromhex('FF D8 FF'), 0)
    write_repaired(jpeg_out, jpeg_out, b'\x00\x00',
                   bytes.fromhex('FF D9'), 0, ending=True)

    # MP4: the first ISO BMFF atom must be 'ftyp', not 'pfyt'.
    write_repaired(args.file3, args.out/'file3.mp4', b'pfyt', b'ftyp', 4)
    print('\nOpen the three repaired files and read their visible flag segments.')


if __name__ == '__main__':
    main()
