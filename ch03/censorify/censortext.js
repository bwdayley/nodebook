var censoredWords = ["sad", "bad", "mad"];
function censor(inStr) {
  for (idx in censoredWords) {
    inStr = inStr.replace(censoredWords[idx], "****");
  }
  return inStr;
}
exports.censor = censor;
exports.censoredWords = censoredWords;