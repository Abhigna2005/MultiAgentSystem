"""Addendum A (S12): the oracle_v3_no_modifier policy and the decomp arm
registry match PROTOCOL_addendum_A.md. No LLM calls."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validation/round2"))

from oracle.action_modifier import NoOpActionModifier
from simulation_runner import _build_agent_for_policy


def test_oracle_v3_no_modifier_wiring():
    agent = _build_agent_for_policy("oracle_v3_no_modifier", 10)
    board = agent.boardroom
    assert board.oracle_mode == "oracle_v3"
    assert board.use_oracle is True
    assert board.enable_action_modifier is False
    assert isinstance(board.action_modifier, NoOpActionModifier)
    assert board.oracle.mode == "oracle_v3"
    assert board.oracle.enable_memory_retrieval is True
    assert board.oracle.brief_version == "v1"


def test_noop_modifier_leaves_actions_unchanged():
    action = {"marketing": {"spend": 5000.0},
              "product": {"r_and_d_spend": 2000.0},
              "hiring": {"hires": 1}}
    assert NoOpActionModifier().modify(action, brief=None) == action


