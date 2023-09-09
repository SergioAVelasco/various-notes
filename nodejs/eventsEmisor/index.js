const Emmitter = require("./emitter");
const { SAVE } = require("./event-names");
const { EventEmitter } = require("events");

//Custom events
const emmitter = new Emmitter();

emmitter.on(SAVE, () => {
  console.log("On save 1");
});

emmitter.on(SAVE, () => {
  console.log("On save 2");
});

emmitter.emit(SAVE);

//System events
const eventEmitter = new EventEmitter();

eventEmitter.on(SAVE, () => {
  console.log("On save 1");
});

eventEmitter.on(SAVE, () => {
  console.log("On save 2");
});

eventEmitter.emit(SAVE);
