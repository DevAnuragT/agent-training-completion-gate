import unittest
from agent import analyze
def p(): return {"today":"2026-09-29","courses":[{"name":"Safety","required":True,"completed":True,"expires_on":"2027-01-01"}]}
class Tests(unittest.TestCase):
 def test_complete(self): self.assertEqual(analyze(p())["status"],"complete")
 def test_valid(self): self.assertTrue(analyze(p())["courses"][0]["valid"])
 def test_incomplete(self): x=p(); x["courses"][0]["completed"]=False; self.assertEqual(analyze(x)["status"],"incomplete")
 def test_expired(self): x=p(); x["courses"][0]["expires_on"]="2026-09-28"; self.assertEqual(analyze(x)["status"],"incomplete")
 def test_optional(self): x=p(); x["courses"][0]["required"]=False; x["courses"][0]["completed"]=False; self.assertEqual(analyze(x)["status"],"complete")
 def test_no_expiry(self): x=p(); x["courses"][0]["expires_on"]=None; self.assertEqual(analyze(x)["status"],"complete")
 def test_bad_date(self): x=p(); x["today"]="today"; self.assertRaises(ValueError,analyze,x)
 def test_bool(self): x=p(); x["courses"][0]["completed"]=1; self.assertRaises(ValueError,analyze,x)
 def test_duplicate(self): x=p(); x["courses"].append(x["courses"][0]); self.assertRaises(ValueError,analyze,x)
if __name__=="__main__": unittest.main()
