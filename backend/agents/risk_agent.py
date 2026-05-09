from backend.services.llm_service import ask_llm


class RiskAgent:

    def analyze(self, shipment_data):

        prompt = f"""
        Analyze the following supply chain data.

        Detect:
        - shipment risks
        - geopolitical threats
        - delay probability
        - supplier instability
        - fuel price impact

        Data:
        {shipment_data}

        Return:
        - risk level
        - explanation
        - mitigation steps
        """

        return ask_llm(prompt)
