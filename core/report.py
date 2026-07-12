from datetime import datetime
import os


class ReportGenerator:

    def save(self, analysis):

        os.makedirs("outputs", exist_ok=True)

        filename = datetime.now().strftime(
            "outputs/study_report_%Y%m%d_%H%M%S.txt"
        )

        with open(filename, "w", encoding="utf-8") as report:

            report.write("=====================================\n")
            report.write("        FocusLens Study Report\n")
            report.write("=====================================\n\n")

            report.write(f"Generated : {datetime.now()}\n\n")

            report.write(f"Study Status      : {analysis['status']}\n")
            report.write(f"Focus Score       : {analysis['score']}%\n")
            report.write(f"Focus Level       : {analysis['level']}\n")
            report.write(f"Session Duration  : {analysis['session_time']}\n")
            report.write(f"Distractions      : {analysis['distraction_count']}\n")
            report.write(f"Phone Usage       : {analysis['phone_time']}\n\n")

            report.write("Recommendation\n")
            report.write("-------------------------\n")

            if analysis["suggestions"]:
                report.write(analysis["suggestions"][0])
            else:
                report.write("No suggestions.")

        return filename