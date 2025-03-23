function score_CF(rating, easy, medium, hard, acceptance, weekly) {
  // Codeforces
  return (
    (((rating - 2250) / 1600) * 1650 +
      (easy / 500) * 450 +
      (medium / 430) * 960 +
      (hard / 550) * 1660 +
      (acceptance / 100) * 50 +
      (weekly / 50) * 85 +
      2450) /
    500
  );
}

function score_LC(ranking, easy, medium, hard, acceptance, weekly) {
  // Leetcode
  return (
    ((ranking - 40) / 5000000) * -30 +
    (easy / 840) * 15 +
    (medium / 1770) * 60 +
    (hard / 790) * 8 +
    (acceptance / 100) * 10 +
    (weekly / 344) * 15 +
    25
  );
}

// Currently take both platforms as equal and just add the score
