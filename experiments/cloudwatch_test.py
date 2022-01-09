

import pandas as pd
from datetime import datetime, timedelta, timezone

from CloudWatch import CloudWatch
start = datetime(year=2022, month=1, day=9, hour=16, minute=47, second=58, tzinfo=timezone.utc)
end = datetime(year=2022, month=1, day=9, hour=16, minute=51, second=16, tzinfo=timezone.utc)


cloudwatch = CloudWatch()

# result = cloudwatch.get_metric_data(metric_name='Invocations', start=start, end=end)
# print(result)
statistic = 'Sum'
period = 1
# error_count = cloudwatch.get_statistics(metric_name='Errors', statistic=statistic, start=start, end=end, period=period)
invocation_count = cloudwatch.get_statistics(metric_name='Invocations', statistic=statistic, start=start, end=end, period=period)
# throttle_count = cloudwatch.get_statistics(metric_name='Throttles', statistic=statistic, start=start, end=end, period=period)

# if invocation_count > 0:
#     error_rate = error_count / invocation_count
# else:
#     error_rate = 0

print(invocation_count)
# print(error_rate)
# print(throttle_count)


