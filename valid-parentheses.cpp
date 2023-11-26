// Solution to https://leetcode.com/problems/valid-parentheses/
// Amal George M
class Solution {
public:
    bool isValid(string s) {
        if (!s.empty())
        {
            string temp;
            try
            {
            for(long i=0;i<s.length();i++){
                if(isClossingbrace(s[i]))
                {
                    if (!temp.empty()){
                    if (isCorrectClosingBracket(temp.back(),s[i]))
                    {
                        temp.pop_back();
                    }
                    else return false;
                    }
                    else return false;
                }
                else
                {
                    temp.push_back(s[i]);
                }
            }
            }
            catch (...)
            {
                return false;
            }
            if(temp.empty()) return true;
        }
        return false;
    }
private:
    bool isClossingbrace(char a){
        switch(a){
            case '}':
            case ']':
            case ')': return true;
            default: return false;
        }
    }
    bool isCorrectClosingBracket(char a, char b){
        switch(a){
            case '{': return((b=='}')?true:false);
            case '(': return((b==')')?true:false);
            case '[': return((b==']')?true:false);
            default: return false;
        }
    }
};
