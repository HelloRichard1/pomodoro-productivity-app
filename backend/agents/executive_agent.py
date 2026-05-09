from backend.services.llm_service import ask_llm


class ExecutiveAgent:

    def summarize(self, reports):

        prompt = f"""
        Create a concise executive briefing.

        Include:
        - major threats
        - projected losses
        - operational impact
        - recommendations
        - confidence score

        Reports:
        {reports}
        """

        return ask_llm(prompt)
