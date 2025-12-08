from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class OwlRole(str, Enum):
    OPER = "Oper"    # Perception
    OACT = "Oact"    # Action
    OCOM = "Ocom"    # Communication
    OPLAN = "Oplan"  # Planning
    OREA = "Orea"    # Reasoning
    OMETA = "Ometa"  # Meta-control
    OMEM = "Omem"    # Memory
    OWORLD = "Oworld"  # World model
    OETH = "Oeth"    # Ethics / safety


@dataclass
class OwlSpec:
    """
    Specification for a single Owl agent role.
    """
    role: OwlRole
    tier: str          # "operational", "strategic", "foundational"
    short_name: str
    description: str


def default_owl_specs() -> List[OwlSpec]:
    """
    Return the canonical set of 9 Owl role specifications.
    """
    return [
        OwlSpec(
            role=OwlRole.OPER,
            tier="operational",
            short_name="Perception",
            description="Multimodal encoding into latent space.",
        ),
        OwlSpec(
            role=OwlRole.OACT,
            tier="operational",
            short_name="Action",
            description="Tool use, API calls, external actuation.",
        ),
        OwlSpec(
            role=OwlRole.OCOM,
            tier="operational",
            short_name="Communication",
            description="Dialogue with users, explanation, external language interface.",
        ),
        OwlSpec(
            role=OwlRole.OPLAN,
            tier="strategic",
            short_name="Planning",
            description="Goal decomposition, search over futures, plan refinement.",
        ),
        OwlSpec(
            role=OwlRole.OREA,
            tier="strategic",
            short_name="Reasoning",
            description="Logical checks, consistency analysis, counterexample search.",
        ),
        OwlSpec(
            role=OwlRole.OMETA,
            tier="strategic",
            short_name="Meta",
            description="Global control of coupling and temperature; monitors uncertainty.",
        ),
        OwlSpec(
            role=OwlRole.OMEM,
            tier="foundational",
            short_name="Memory",
            description="Long-term memory, retrieval, episodic context.",
        ),
        OwlSpec(
            role=OwlRole.OWORLD,
            tier="foundational",
            short_name="WorldModel",
            description="Predictive modeling of environment dynamics.",
        ),
        OwlSpec(
            role=OwlRole.OETH,
            tier="foundational",
            short_name="Ethics",
            description="Values, constraints, and veto power over unsafe or misaligned plans.",
        ),
    ]
