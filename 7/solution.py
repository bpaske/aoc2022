from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    files: List[File] = field(default_factory=list)
    children: Dict[str, "Directory"] = field(default_factory=dict)
    parent: Optional["Directory"] = None
    total_size: Optional[int] = None

    def add_child(self, name):
        self.children[name] = Directory(
            name=name,
            parent=self,
        )

    def get_child(self, name):
        return self.children[name]

    def add_file(self, name, size):
        self.files.append(File(name, size))


with open("./input.txt") as f:
    root = Directory(name="/")
    current_dir = root
    for instruction in f.read().splitlines()[1:]:
        if instruction.startswith("$ cd"):
            target_dir = instruction.split(" ")[-1]
            if target_dir == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(target_dir)
        elif instruction.startswith("$ ls"):
            pass
        elif instruction.startswith("dir "):
            current_dir.add_child(instruction.split(" ")[-1])
        else:  # files
            size, name = instruction.split(" ")
            current_dir.add_file(name, int(size))


def calculate_total_size(node: Directory):
    if node.total_size == None:
        total_size = sum(f.size for f in node.files) + sum(
            calculate_total_size(d) for d in node.children.values()
        )
        node.total_size = total_size
        return total_size
    else:
        return node.total_size


def sum_less_hundred_thousand(node: Directory):
    children_sum = sum(sum_less_hundred_thousand(c) for c in node.children.values())
    return children_sum if node.total_size > 100000 else children_sum + node.total_size


calculate_total_size(root)
print(f"Part 1 answer: {sum_less_hundred_thousand(root)}")

required_free_space = 30000000
total_space = 70000000
current_free_space = total_space - root.total_size
space_needed_to_delete = required_free_space - current_free_space


def find_closest_diff_above(node: Directory, required_size: int):
    diffs = (
        [node.total_size - required_size]
        + [find_closest_diff_above(c, required_size) for c in node.children.values()]
        + [float("inf")]
    )
    return min(diff for diff in diffs if diff > 0)


part_2_answer = space_needed_to_delete + find_closest_diff_above(
    root, space_needed_to_delete
)
print(f"Part 2 answer: {part_2_answer}")
