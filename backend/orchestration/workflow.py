from langgraph.graph import StateGraph
from backend.agents.risk_agent import RiskAgent
from backend.agents.negotiation_agent import NegotiationAgent
from backend.agents.executive_agent import ExecutiveAgent

risk_agent = RiskAgent()
negotiation_agent = NegotiationAgent()
executive_agent = ExecutiveAgent()


class WorkflowState(dict):
    pass


def run_risk_analysis(state):
    result = risk_agent.analyze(state["shipment_data"])
    state["risk_report"] = result
    return state


def run_negotiation(state):
    result = negotiation_agent.negotiate(state["supplier_data"])
    state["negotiation_report"] = result
    return state


def run_executive_summary(state):
    reports = f"""
    {state["risk_report"]}

    {state["negotiation_report"]}
    """

    result = executive_agent.summarize(reports)
    state["executive_summary"] = result
    return state

workflow = StateGraph(WorkflowState)
workflow.add_node("risk", run_risk_analysis)
workflow.add_node("negotiation", run_negotiation)
workflow.add_node("summary", run_executive_summary)
workflow.set_entry_point("risk")
workflow.add_edge("risk", "negotiation")
workflow.add_edge("negotiation", "summary")

graph = workflow.compile()
