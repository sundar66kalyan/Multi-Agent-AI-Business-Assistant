from pathlib import Path


class ChartService:

    @staticmethod
    def revenue_chart(finance: dict):

        # Import only when a chart is actually generated
        import matplotlib.pyplot as plt

        reports = Path("reports")
        reports.mkdir(exist_ok=True)

        output = reports / "revenue_chart.png"

        labels = ["Revenue", "Expenses", "Profit"]

        values = [
            finance["revenue"],
            finance["expenses"],
            finance["profit"],
        ]

        plt.figure(figsize=(6, 4))
        plt.bar(labels, values)
        plt.title("Financial Summary")
        plt.ylabel("Amount")
        plt.tight_layout()
        plt.savefig(output)
        plt.close()

        return str(output)