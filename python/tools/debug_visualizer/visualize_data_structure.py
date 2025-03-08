import json
from dataclasses import dataclass
from typing import Callable, Generic, List, TypeVar


@dataclass
class NodeMetadata:
    """Class for storing metadata about a data structure node"""

    id: str
    label: str
    # color: str


@dataclass
class EdgeMetadata:
    """Class for storing metadata about a data structure edge"""

    from_id: str
    to_id: str
    # color: str


T = TypeVar("T")


def visualize_data_structure(
    ds: Generic[T],
    node_mapper: Callable[[T], List[NodeMetadata]],
    edge_mapper: Callable[[T], List[EdgeMetadata]],
):
    """Serialize a data structure like a linked list or tree into a format the visualizer can understand."""
    node_metadata_list = node_mapper(ds)
    edge_metadata_list = edge_mapper(ds)
    formatted = {
        "kind": {"graph": True},
        "nodes": [{"id": node.id, "label": node.label} for node in node_metadata_list],
        "edges": [
            {"from": node.from_id, "to": node.to_id} for node in edge_metadata_list
        ],
    }
    return json.dumps(formatted)
