function submit() {
  const ask_amount = document.getElementById("ask_amount").value;
  const ask_equity = document.getElementById("max_equity").value;
  const ask_valuation = document.getElementById("ask_valuation").value;

  window.location.href = `/predict?ask_amount=${ask_amount}&ask_equity=${ask_equity}&ask_valuation=${ask_valuation}&probabilities=true`;
}
