#!/usr/bin/env python3

import json
import argparse
import os
import re


class Publication:
    def __init__(self):
        self.id = None
        self.title = None
        self.authors = []
        self.year = None
        self.url = None
        self.doi = None
        self.journal = None
        self.booktitle = None
        self.pages = ""
        self.volume = None
        self.type = None
        self.bibType = None

    def md(self):
        res = ["---"]
        for key in (
            "id",
            "title",
            "authors",
            "year",
            "url",
            "doi",
            "journal",
            "booktitle",
            "pages",
            "volume",
            "type",
            "bibType",
        ):
            value = getattr(self, key)
            if value is not None:
                res.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
        res.append("---")
        return "\n".join(res)

    def set_attribute_from_ris(self, key, value):
        if key == "TY":
            if value not in ["JOUR", "CPAPER"]:
                return
            self.type = "journal" if value == "JOUR" else "conference"
            self.bibType = "article" if value == "JOUR" else "inproceedings"
        elif key == "AU":
            last, first = value.split(", ")
            self.authors.append(first + " " + last)
        elif key == "TI":
            self.title = value
        elif key == "BT":
            self.booktitle = value
        elif key == "JO":
            self.journal = value
        elif key == "SP":
            self.pages = value + "-" + self.pages
        elif key == "EP":
            self.pages = self.pages + value
        elif key == "VL":
            self.volume = value
        elif key == "PY":
            self.year = value[: value.find("/")]
        elif key == "DO":
            self.doi = value
        elif key == "UR":
            self.url = value
        elif key == "ID":
            self.id = re.sub(r"[^\w]", "_", value.split(":")[-1].strip())


def parse_ris(ris):
    ris = ris.split("\n\n")
    if not ris[0].strip().startswith("TY"):
        del ris[0]
    result = []
    for i in range(len(ris)):
        if ris[i].strip() == "":
            continue
        pub = Publication()
        lines = ris[i].strip().split("\n")
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            j = line.find("-")
            if j == -1:
                continue
            key = line[:j].strip()
            value = line[j + 1 :].strip()
            if value == "":
                continue
            pub.set_attribute_from_ris(key, value)
        if pub.type is not None:
            result.append(pub)
    return result


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("ris")
    p.add_argument("outDir", nargs="?", default=os.getcwd())
    p.add_argument("--titles", "-t", action="store_true")
    args = p.parse_args()
    with open(args.ris, "r") as f:
        pubs = parse_ris(f.read())
    if not os.path.isdir(args.outDir):
        os.makedirs(args.outDir)
    if args.titles:
        for pub in pubs:
            print(pub.title)
    else:
        for pub in pubs:
            with open(os.path.join(args.outDir, pub.id) + ".md", "w") as f:
                f.write(pub.md())

