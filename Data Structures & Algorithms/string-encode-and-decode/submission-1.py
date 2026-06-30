class Solution:

    def encode(self, strs: List[str]) -> str:
        return "EMPTY_LIST_MARKER" if not strs else "{J}".join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if s == "EMPTY_LIST_MARKER" else s.split("{J}")
