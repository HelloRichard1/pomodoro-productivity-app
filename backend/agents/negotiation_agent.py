from backend.services.llm_service import ask_llm


class NegotiationAgent:

    def negotiate(self, supplier_info):

        prompt = f"""
        You are an autonomous procurement negotiator.

        Goal:
        Reduce cost while maintaining delivery deadlines.

        Supplier Data:
        {supplier_info}

        Generate:
        - negotiation strategy
        - pricing arguments
        - urgency leverage
        - fallback suppliers
        """

        return ask_llm(prompt)
