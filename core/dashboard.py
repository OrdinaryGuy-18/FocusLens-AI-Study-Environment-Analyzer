import cv2


class Dashboard:

    def draw(self, frame, analysis):

        h, w = frame.shape[:2]

        # =========================
        # HEADER
        # =========================

        cv2.rectangle(
            frame,
            (0, 0),
            (w, 60),
            (35, 35, 35),
            -1
        )

        cv2.putText(
            frame,
            "FocusLens - AI Study Environment Analyzer",
            (20, 38),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.85,
            (255, 255, 255),
            2
        )

        # =========================
        # BOTTOM DASHBOARD
        # =========================

        dashboard_height = 150

        cv2.rectangle(
            frame,
            (0, h - dashboard_height),
            (w, h),
            (35, 35, 35),
            -1
        )

        # -------------------------
        # STATUS
        # -------------------------

        status_color = (0, 200, 0)

        if analysis["status"] == "PAUSED":
            status_color = (0, 0, 255)

        cv2.putText(
            frame,
            f"Status : {analysis['status']}",
            (20, h - 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            status_color,
            2
        )

        cv2.putText(
            frame,
            f"Session : {analysis['session_time']}",
            (20, h - 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        # -------------------------
        # SCORE
        # -------------------------

        cv2.putText(
            frame,
            f"Focus Score : {analysis['score']}%",
            (300, h - 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Distractions : {analysis['distraction_count']}",
            (300, h - 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Phone Usage : {analysis['phone_time']}",
            (300, h - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        # -------------------------
        # LEVEL
        # -------------------------

        cv2.putText(
            frame,
            f"Level : {analysis['level']}",
            (620, h - 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # =========================
        # PROGRESS BAR
        # =========================

        bar_x = 20
        bar_y = h - 28

        bar_width = 420
        bar_height = 18

        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + bar_width, bar_y + bar_height),
            (120, 120, 120),
            2
        )

        filled = int(bar_width * analysis["score"] / 100)

        if analysis["score"] >= 70:
            color = (0, 220, 0)

        elif analysis["score"] >= 40:
            color = (0, 220, 220)

        else:
            color = (0, 0, 255)

        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + filled, bar_y + bar_height),
            color,
            -1
        )

        # Draw percentage on progress bar

        cv2.putText(
            frame,
            f"{analysis['score']}%",
            (bar_x + 180, bar_y + 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

        # =========================
        # RECOMMENDATION
        # =========================

        cv2.putText(
            frame,
            "Recommendation",
            (500, h - 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (0, 255, 255),
            2
        )

        recommendation = "Ready to study."

        if analysis["suggestions"]:
            recommendation = analysis["suggestions"][0]

        cv2.putText(
            frame,
            recommendation,
            (500, h - 18),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )

        return frame