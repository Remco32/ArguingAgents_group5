#Creates corpera files from scraped websites.
#Make sure there is no existing corpera yet (i.e. Corpus folder does not exist)

from CorpusConverters import convert_json_to_corpus_shortArguments_procon
from CorpusConverters import convert_json_to_corpus_longArguments_procon
from CorpusConverters import convert_json_to_corpus_debatabase
from CorpusConverters import combine_corpus

convert_json_to_corpus_shortArguments_procon()
convert_json_to_corpus_longArguments_procon()
convert_json_to_corpus_debatabase()
combine_corpus()