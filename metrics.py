class MetricsTracker:

    def __init__(self):

        self.total_requests = 0
        self.success_count = 0
        self.failure_count = 0

        self.validation_failures = 0
        self.repairs = 0

        self.total_latency = 0

    def record(
        self,
        success,
        latency,
        validation_failed=False,
        repaired=False
    ):

        self.total_requests += 1

        self.total_latency += latency

        if success:
            self.success_count += 1
        else:
            self.failure_count += 1

        if validation_failed:
            self.validation_failures += 1

        if repaired:
            self.repairs += 1

    def report(self):

        avg_latency = 0

        if self.total_requests > 0:
            avg_latency = (
                self.total_latency
                / self.total_requests
            )

        return {
            "total_requests":
                self.total_requests,

            "success_rate":
                round(
                    self.success_count
                    / max(1, self.total_requests)
                    * 100,
                    2
                ),

            "failure_rate":
                round(
                    self.failure_count
                    / max(1, self.total_requests)
                    * 100,
                    2
                ),

            "validation_failures":
                self.validation_failures,

            "repairs":
                self.repairs,

            "average_latency":
                round(avg_latency, 2)
        }