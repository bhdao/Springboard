const createInstructor = (firstName, lastName) => {
  return {
    firstName,
    lastName
  }
};

const instructor = {
  firstName: "Andy",
  [5 + 5]: "That's my favorite number!"
};

const manager = {
  firstName: "Super",
  lastName: "Bossman",
  whoIsTheBoss(firstName, lastName) {
    return `${firstName} ${lastName} is the boss!`
  }
}

const makeAnimal = (species, command, sound) => {
  return {
    species,
    [command]() {
      return sound
    }
  }
};