class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "\U0001F681"
        sep = "\U0001F680"
        return sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "\U0001F681":
            return []
        sep = "\U0001F680"
        return s.split(sep)
