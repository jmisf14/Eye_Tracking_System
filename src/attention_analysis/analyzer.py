class AttentionAnalyzer:
    def __init__(self):
        self.gaze_data = []

    def analyze_attention(self, gaze_data):
        self.gaze_data = gaze_data
        attention_score = self.calculate_attention_score()
        return attention_score

    def calculate_attention_score(self):
        # Placeholder for attention score calculation logic
        if not self.gaze_data:
            return 0
        # Example logic: count the number of fixations on products
        fixations_on_products = sum(1 for gaze in self.gaze_data if gaze['on_product'])
        return fixations_on_products / len(self.gaze_data)

    def generate_report(self):
        attention_score = self.calculate_attention_score()
        report = {
            'attention_score': attention_score,
            'gaze_data': self.gaze_data
        }
        return report