var GLASSOCT = {
  count: 0,
  glasses: {},
};

class Octopus {
  x;
  y;
  head;
  tail;
  parent;
  config;
  defaultConfig = {
    radius: 7,
    margin: 5,
    headColor: "#42e39d",
    tailColor: null,
    headOpacity: 1,
    tailOpacity: 0.5,
    positionUnit: "px",
  };
  defaultConfigKeys = Object.keys(this.defaultConfig);

  num2string(num) {
    return parseInt(num).toString();
  }

  position(element, radius, x, y, unit) {
    if (unit == "%") {
      x = (this.parent.image.width * x) / 100;
      y = (this.parent.image.height * y) / 100;
    }
    element.style.left = this.num2string(x - radius) + "px";
    element.style.top = this.num2string(y - radius) + "px";
  }

  circularise(element, radius) {
    element.style.width = this.num2string(radius * 2) + "px";
    element.style.height = this.num2string(radius * 2) + "px";
    element.style.borderRadius = this.num2string(radius) + "px";
  }

  updatePosition() {
    this.position(
      this.head,
      this.config.radius,
      this.x,
      this.y,
      this.config.positionUnit
    );
    this.position(
      this.tail,
      this.config.radius + this.config.margin,
      this.x,
      this.y,
      this.config.positionUnit
    );
  }

  constructor(x, y, config, parentObj) {
    if (!config) config = {};

    for (let ki in this.defaultConfigKeys) {
      var key = this.defaultConfigKeys[ki];
      if (!(key in config)) config[key] = this.defaultConfig[key];
    }

    if (config.tailColor === null) config.tailColor = config.headColor;

    // -------------------------------------------- //

    this.x = x;
    this.y = y;
    this.config = config;
    this.parent = parentObj;

    // -------------------------------------------- //

    this.head = document.createElement("div");

    this.circularise(this.head, config.radius);
    this.head.style.backgroundColor = config.headColor;
    this.head.style.opacity = config.headOpacity;
    this.head.classList.add("glass-oct-head");

    // -------------------------------------------- //

    this.tail = document.createElement("div");

    this.circularise(this.tail, config.radius + config.margin);
    this.tail.style.backgroundColor = config.tailColor;
    this.tail.style.opacity = config.tailOpacity;
    this.tail.classList.add("glass-oct-tail");

    // -------------------------------------------- //

    this.updatePosition();

    this.parent.octopusesTank.appendChild(this.head);
    this.parent.octopusesTank.appendChild(this.tail);

    return this;
  }
}

class Glass {
  id;
  parentContainer;
  container;
  rszObs;
  image;
  octopusesTank;
  octopusCount = 0;
  octopuses = {};
  loaded = false;

  updateOctopuses() {
    var octKeys = Object.keys(this.octopuses);
    for (let ki in octKeys) {
      let oct = this.octopuses[octKeys[ki]];
      oct.updatePosition();
    }
  }

  constructor(imagePath) {
    this.image = document.createElement("img");
    this.image.src = imagePath;
    this.image.classList.add("glass-oct-img");

    this.id = GLASSOCT.count;
    GLASSOCT.glasses[this.id] = this;
    GLASSOCT.count += 1;

    this.image.setAttribute("glassoct-parent", this.id);
    this.image.onload = function () {
      var parentId = this.getAttribute("glassoct-parent");
      GLASSOCT.glasses[parentId].updateOctopuses();
    };

    this.rszObs = new ResizeObserver(function (entries) {
      entries.forEach((entry) => {
        var parentId = entry.target.getAttribute("glassoct-parent");
        GLASSOCT.glasses[parentId].updateOctopuses();
      });
    });
    this.rszObs.observe(this.image);
  }

  attach(element, fit) {
    if (!fit) fit = "contain";

    this.image.style.object_fit = fit;

    this.parentContainer = element;
    this.container = document.createElement("div");
    this.parentContainer.appendChild(this.container);

    this.container.classList.add("glass-oct-cont");
    this.container.appendChild(this.image);
    this.container.setAttribute("glassoct-parent", this.id);
    this.container.onresize = function () {
      console.log("resized");
      var parentId = this.getAttribute("glassoct-parent");
      GLASSOCT.glasses[parentId].updateOctopuses();
    };

    this.octopusesTank = document.createElement("div");
    this.octopusesTank.setAttribute("name", "octopuses");
    this.octopusesTank.style.position = "none";
    this.container.appendChild(this.octopusesTank);
  }

  addOctopus(x, y, config) {
    if (!config) config = {};

    var newOct = new Octopus(x, y, config, this);

    this.octopuses[this.octopusCount] = newOct;
    this.octopusCount += 1;

    return [this.octopusCount, newOct];
  }
}

function injectGlass(element, imagePath) {
  var newGlass = new Glass(imagePath);
  newGlass.attach(element);
  return newGlass;
}
