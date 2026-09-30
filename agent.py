"""Evaluate required training completion and expiry against a supplied date."""
from datetime import date
def _date(v,n):
    if not isinstance(v,str): raise ValueError(n+" must be YYYY-MM-DD")
    try: return date.fromisoformat(v)
    except ValueError: raise ValueError(n+" must be YYYY-MM-DD")
def analyze(payload:dict)->dict:
    if not isinstance(payload,dict) or not isinstance(payload.get("courses"),list): raise ValueError("courses must be a list")
    today=_date(payload.get("today"),"today"); out=[]; seen=set()
    for c in payload["courses"]:
        if not isinstance(c,dict) or set(c)!={"name","required","completed","expires_on"}: raise ValueError("invalid course shape")
        name=c["name"]
        if not isinstance(name,str) or not name.strip() or name in seen: raise ValueError("course names must be unique")
        if not isinstance(c["required"],bool) or not isinstance(c["completed"],bool): raise ValueError("required and completed must be booleans")
        expires=None if c["expires_on"] is None else _date(c["expires_on"],"expires_on")
        expired=expires is not None and expires<today; valid=c["completed"] and not expired
        seen.add(name); out.append({"name":name,"required":c["required"],"completed":c["completed"],"expires_on":c["expires_on"],"expired":expired,"valid":valid})
    missing=[x["name"] for x in out if x["required"] and not x["valid"]]
    return {"status":"complete" if not missing else "incomplete","missing_or_invalid":missing,"courses":out,"training_action_taken":False,"basis":"required courses must be completed and not expired on caller-supplied today"}
