class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=='(' or  i=='['or  i=='{':
                st.append(i)
            else:
                match i:
                    case ')':
                        if len(st)>=1:
                            if st[-1]!='(':
                                return False
                            else:
                                st.pop()
                        else:
                            return False
                    case '}':
                        if len(st)>=1:
                            if st[-1]!='{':
                                return False
                            else:
                                st.pop()
                        else:
                            return False
                    case ']':
                        if len(st)>=1:
                            if st[-1]!='[':
                                return False
                            else:
                                st.pop()
                        else:
                            return False
        if len(st)<=0:
            return True
        else:
            return False    
                