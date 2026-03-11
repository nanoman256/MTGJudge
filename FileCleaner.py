import re
#TODO complete this orchestrator after the basic rules are solved and the keywords are implemented

class MTG_Judge:
    def __init__(self, file_path, pattern):
        #member variables included here
        self.m_regex_pattern = pattern
        self.m_file_path = file_path
        self.m_text = None
        with open(self.m_file_path, encoding="utf-8", errors="ignore") as f:
            self.m_text = f.read()
        self.matches = re.findall(self.m_regex_pattern, self.m_text, flags=re.MULTILINE)

        pass
    def askJudge(self):
        #gets prompt
        pass
    def initializeJudgeModel(self):
        pass
    def embedRules(self, filePath):
        pass

    def setRulePattern(self, new_pattern):
        m_regex_pattern = new_pattern
        pass

    def embedPrompt(self): #should return the result
        pass