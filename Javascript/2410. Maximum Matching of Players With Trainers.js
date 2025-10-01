/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function (players, trainers) {
  players.sort((a, b) => a - b);
  trainers.sort((a, b) => a - b);

  let trainerPointer = trainers.length - 1;
  let playerPointer = players.length - 1;
  let res = 0;

  while (playerPointer >= 0) {
    if (players[playerPointer] <= trainers[trainerPointer]) {
      res += 1;
      playerPointer -= 1;
      trainerPointer -= 1;
    } else {
      playerPointer -= 1;
    }
  }

  return res;
};
