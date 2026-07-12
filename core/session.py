import time


class StudySession:

    def __init__(self):

        self.start_time = time.time()

        self.phone_detected_since = None

        self.total_phone_time = 0

        self.distraction_count = 0

    def update(self, analysis):

        current_time = time.time()

        # ---------------- Phone Timer ----------------

        if analysis["phone"]:

            if self.phone_detected_since is None:

                self.phone_detected_since = current_time

                self.distraction_count += 1

        else:

            if self.phone_detected_since is not None:

                self.total_phone_time += (
                    current_time - self.phone_detected_since
                )

                self.phone_detected_since = None

        # -------- Live Phone Usage --------

        live_phone_time = self.total_phone_time

        if self.phone_detected_since is not None:
            live_phone_time += (
                current_time - self.phone_detected_since
            )

        phone_seconds = int(live_phone_time)

        phone_minutes = phone_seconds // 60
        phone_seconds = phone_seconds % 60

        # ---------------- Session Timer ----------------

        elapsed = int(current_time - self.start_time)

        session_minutes = elapsed // 60
        session_seconds = elapsed % 60

        # ---------------- Update Analysis ----------------

        analysis["session_time"] = (
            f"{session_minutes:02}:{session_seconds:02}"
        )

        analysis["phone_time"] = (
            f"{phone_minutes:02}:{phone_seconds:02}"
        )

        analysis["distraction_count"] = self.distraction_count

        return analysis