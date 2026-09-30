# Decision and Reasoning

The result is complete when every required course is completed and either has no expiry or expires on or after today. Optional incomplete courses do not block the gate, while missing or expired required courses do. The implementation returns structured findings so a reviewer can see how each result was derived.

# Inputs and Data Sources

The caller supplies unique course names, required and completed booleans, optional YYYY-MM-DD expiry dates, and a YYYY-MM-DD today value. All date comparisons are calendar-date comparisons with no machine clock access. The only data source is the caller-provided payload plus the checked-in rules and code; no network or private-file access is used.

# Known Limitations and Constraints

This core cannot verify course identity, attendance, assessment scores, equivalence, or whether an expiry policy is appropriate. It does not notify learners, update a learning system, grant access, or provide employment or legal advice. The result is a bounded pre-review aid and must not be presented as professional certification or an official HiDevs result.
