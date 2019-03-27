from fastai.text import *
import sentencepiece as spm
from pathlib import Path

path = Path(__file__).parent


class LanguageTokenizer(BaseTokenizer):
    def __init__(self, lang: str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        model_path = path/f'models/{lang}/tokenizer.model'
        self.sp.Load(str(model_path))

    def tokenizer(self, t: str) -> List[str]:
        return self.sp.EncodeAsPieces(t)


class AllLanguageTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class SanskritTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class BengaliTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class GujaratiTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class HindiTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class KannadaTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class MalyalamTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class MarathiTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class NepaliTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class OriyaTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)


class PanjabiTokenizer(LanguageTokenizer):
    def __init__(self, lang: str):
        LanguageTokenizer.__init__(self, lang)

