class FocusAnalyzer:

    def analyze(self, detected_objects):

        score = 0
        MAX_SCORE = 80
        suggestions = []
        study_status = "Inactive"

        person = "person" in detected_objects
        phone = "cell phone" in detected_objects
        book = "book" in detected_objects

        if person:
            score += 60

        if book:
            score += 20

        if phone:
            score -= 30
            suggestions.append("Keep your phone away while studying.")

        if person and not phone:
            suggestions.append("Excellent study environment.")

        if not person:
            suggestions.append("Student not detected.")

        score = max(score, 0)
        focus_percentage = int((score / MAX_SCORE) * 100)

        if person:
            study_status = "ACTIVE"
        else:
            study_status = "PAUSED"

        if focus_percentage >= 80:
            level = "Excellent"

        elif focus_percentage >= 60:
            level = "Focused"

        elif focus_percentage >= 30:
            level = "Needs Attention"

        else:
            level = "Distracted"

        if not person:
            suggestions.append("No student detected.")

        if score >= 70:
            suggestions.append("Great focus! Keep it up.")

        return {
            "raw_score": score,
            "score": focus_percentage,
            "status": study_status,
            "level": level,
            "suggestions": suggestions,
            "person": person,
            "phone": phone,
            "book": book
        }