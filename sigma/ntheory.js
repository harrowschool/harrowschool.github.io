// Utility funcs
function swap(a, b) {
  // Swapping with only two variables, might be a bit confusing but it works
  a = b - a;
  b = b - a;
  a = b + a;
  return [a, b];
}

// NTheory funcs
function primesUpto(n) {
  // Sieve of Eratosthenes
  var arr = Array(n + 1).fill(true), ret = [];
  arr[0] = arr[1] = false;
  for (var i = 2; i <= n; i++) {
    if (arr[i]) {
      ret.push(i);
      for (var j = i * 2; j <= n; j += i) arr[j] = false;
    }
  }
  return ret;
}

function mod(a, m) {
  return ((a % m) + m) % m; // this is needed to handle negative numbers
}

function gcd(a, b, showSteps = true, history = null) {
  // Euclidean algorithm
  // For algorithm, refer to https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

  if (a > b) [a, b] = swap(a, b);

  if (a == 0) return b;

  var hist_add = [b, a, Math.floor(b / a), b % a];
  if (showSteps) print(hist_add[0] + " = " + hist_add[1] + " × " + hist_add[2] + " + " + hist_add[3], html=false, color="grey");

  if (history != null) {
    history.push(hist_add);
    return gcd(b % a, a, showSteps, history);
  }

  return gcd(b % a, a, showSteps, null);
}

function viewHistory(hist, color="grey") {
  for (i in hist)
    print(hist[i][0] + " = " + hist[i][1] + " × " + hist[i][2] + " + " + hist[i][3], html=false, color);
}

function extEuc(a, b, showSteps = true) {
  // Use extended euclidean algorithm to find x and y such that ax + by = gcd(a, b)

  function cswap(a, b, cond) {
    if (cond) return swap(a, b);
    return [a, b];
  }

  if (a > b) {
    [a, b] = swap(a, b);
    var reversed = true;
  }

  var hist = [];
  var g = gcd(a, b, false, hist);
  if (showSteps) {
    viewHistory(hist, "grey");
    print("GCD = " + g, html=false, color="grey");
  }

  if (hist.length == 1 || hist.length == 2) {
    if (showSteps)
      print("So " + a + " × " + (-hist[0][2]) + " + " + b + " × " + 1 + " = gcd(" + a + ", " + b + ") = " + g, 
      html=false, color="grey");
    return [cswap(-hist[0][2], 1, reversed), g];
  }

  hist.reverse();
  var alpha = hist[1][1], x = -hist[1][2];
  var beta = hist[1][0], y = 1;
  var alpha_old, x_old, beta_old, y_old;

  if (showSteps) print(g + " = " + alpha + " × " + x + " + " + beta + " × " + y, html=false, color="grey");

  for (var i = 2; i < hist.length; i++) {
    alpha_old = alpha, x_old = x, beta_old = beta, y_old = y;

    alpha = beta, x = y + x_old * (-hist[i][2]);
    beta = hist[i][0], y = x_old;

    if (showSteps) {
      print(
        g + " = (" + hist[i][0] + " + " + hist[i][1] + " × " + (-hist[i][2]) + ") × " + x_old + " + " + beta_old + " × " + y_old
        + " = " + alpha + " × " + x + " + " + beta + " × " + y, html=false, color="grey");
    }
  }

  if (showSteps)
    print("So " + a + " × " + x + " + " + b + " × " + y + " = gcd(" + a + ", " + b + ") = " + g, 
    html=false, color="grey")

  return [cswap(x, y, reversed), g];
}

function inv(a, m, showSteps = true) {
  [[x, y], g] = extEuc(a, m, showSteps);
  if (g != 1) throw a + " and modulus " + m + " are not coprime!";
  else {
    var ret = mod(x, m);  
    if (showSteps) print("So inverse is " + x + " ≡ " + ret + " (mod " + m +")", html=false, color="grey");
    return ret;
  }
}

function totient(n) {
  if (n == 1) return 1;
  if (!(n > 1 && Number.isInteger(n))) return null;
  var ret = 0;
  for (var i=1; i<n; i++) {
    if (gcd(i, n, false, null) == 1) ret += 1;
  }
  return ret;
}
