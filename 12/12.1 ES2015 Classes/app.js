class Vehicle {
  honk() {
    return "honk!";
  }
  toString() {
    return `This vehicle is a ${this.make} ${this.model} from ${this.year}.`;
  }
}

let myFirstVehicle = new Vehicle;
myFirstVehicle.make = "Audi";
myFirstVehicle.model = "5000";
myFirstVehicle.year = 2020;

console.log(myFirstVehicle.honk());
console.log(myFirstVehicle.toString());

class Car extends Vehicle {
  constructor(make, model, year) {
    super();
  }
  numWheels = 4;
}

let myCar = new Car;
myCar.make = "Toyota";
myCar.model = "Corolla";
myCar.year = "2001";

console.log(
  myCar.toString(), '\n',
  myCar.honk(), '\n',
  myCar.numWheels,
)

class Motorcycle extends Car {
  constructor(make, model, year) {
    super();
  };
  numWheels = 2;
  revEngine() { return "Vroommmm!!!" }
};

let myMoto = new Motorcycle;
myMoto.make = "Yamaha";
myMoto.model = "MT-09 SP";
myMoto.year = "2021";


console.log(
  myMoto.toString(), '\n',
  myMoto.honk(), '\n',
  myMoto.numWheels, '\n',
  myMoto.revEngine()
)

class Garage {
  vehicles = [];
  capacity = 3;
  add(vehicle) {
    if (this.vehicles.length < this.capacity) {
      if (vehicle instanceof Vehicle) {
        this.vehicles.push(vehicle);
        console.log(`${vehicle} Successfully added to the garage!`)
      } else {
        throw console.error("Hey! This is not a proper instance of a vehicle!");
      }
    } else {
      throw console.error(`Garage has reached full capacity of ${this.capacity}`);
    }
  }
}