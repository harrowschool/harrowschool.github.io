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
    positionUnit: "%",
  };
  defaultConfigKeys = Object.keys(this.defaultConfig);

  num2string(num) {
    return parseInt(num).toString();
  }

  position(element, radius, x, y, unit) {
    var coords = this.parent.standardUnits(x, y, unit);
    x = coords[0];
    y = coords[1];
    element.style.left = this.num2string(x - radius) + "px";
    element.style.top = this.num2string(y - radius) + "px";
  }

  circularise(element, radius) {
    element.style.width = this.num2string(radius * 2) + "px";
    element.style.height = this.num2string(radius * 2) + "px";
    element.style.borderRadius = this.num2string(radius) + "px";
  }

  update() {
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

    this.update();

    this.parent.octopusesTank.appendChild(this.head);
    this.parent.octopusesTank.appendChild(this.tail);

    return this;
  }
}

class Tentacle {
  targX;
  targY;
  iconImg;
  iconContainer;
  parent;
  config;
  defaultConfig = {
    width: 100,
    anchorX: 0,
    anchorY: 0,
    opacity: 1,
    positionUnit: "%",
    sizeUnit: "px",
    anchorUnit: "%",
  };
  defaultConfigKeys = Object.keys(this.defaultConfig);

  num2string(num) {
    return parseInt(num).toString();
  }

  standardUnits(x, y, unit) {
    if (unit == "%") {
      x = (this.iconImg.width * x) / 100;
      y = (this.iconImg.height * y) / 100;
    }
    return [x, y];
  }

  position() {
    var tcoords = this.parent.standardUnits(
      this.targX,
      this.targY,
      this.config.positionUnit
    );
    var tx = tcoords[0];
    var ty = tcoords[1];

    var aCoords = this.standardUnits(
      this.config.anchorX,
      this.config.anchorY,
      this.config.anchorUnit
    );
    var ax = aCoords[0];
    var ay = aCoords[1];

    this.iconContainer.style.left = this.num2string(tx - ax) + "px";
    this.iconContainer.style.top = this.num2string(ty - ay) + "px";

    console.log(ax, ay, tx, ty);
  }

  update() {
    this.position();
  }

  constructor(targX, targY, iconPath, config, parentObj) {
    if (!config) config = {};

    for (let ki in this.defaultConfigKeys) {
      var key = this.defaultConfigKeys[ki];
      if (!(key in config)) config[key] = this.defaultConfig[key];
    }

    if (config.tailColor === null) config.tailColor = config.headColor;

    // -------------------------------------------- //

    this.targX = targX;
    this.targY = targY;
    this.config = config;
    this.parent = parentObj;

    // -------------------------------------------- //

    this.iconContainer = document.createElement("div");
    this.iconContainer.style.opacity = this.config.opacity;
    this.iconContainer.classList.add("glass-oct-tent");

    this.iconImg = document.createElement("img");
    this.iconImg.src = iconPath;
    this.iconImg.style.width =
      this.num2string(this.config.width) + this.config.sizeUnit;

    this.iconContainer.appendChild(this.iconImg);

    this.update();

    this.parent.octopusesTank.appendChild(this.iconContainer);

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
  childrenCount = 0;
  children = {};
  loaded = false;

  updateChildren() {
    var octKeys = Object.keys(this.children);
    for (let ki in octKeys) {
      let oct = this.children[octKeys[ki]];
      oct.update();
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
      GLASSOCT.glasses[parentId].updateChildren();
    };

    this.rszObs = new ResizeObserver(function (entries) {
      entries.forEach((entry) => {
        var parentId = entry.target.getAttribute("glassoct-parent");
        GLASSOCT.glasses[parentId].updateChildren();
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
      GLASSOCT.glasses[parentId].updateChildren();
    };

    this.octopusesTank = document.createElement("div");
    this.octopusesTank.setAttribute("name", "octopuses");
    this.octopusesTank.style.position = "none";
    this.container.appendChild(this.octopusesTank);
  }

  addOctopus(x, y, config) {
    if (!config) config = {};

    var newOct = new Octopus(x, y, config, this);

    this.children[this.childrenCount] = newOct;
    this.childrenCount += 1;

    return [this.childrenCount, newOct];
  }

  addTentacle(targX, targY, iconPath, config) {
    if (!config) config = {};

    var newTcl = new Tentacle(targX, targY, iconPath, config, this);

    this.children[this.childrenCount] = newTcl;
    this.childrenCount += 1;

    return [this.childrenCount, newTcl];
  }

  standardUnits(x, y, unit) {
    if (unit == "%") {
      x = (this.image.width * x) / 100;
      y = (this.image.height * y) / 100;
    }
    return [x, y];
  }
}

function injectGlass(element, imagePath) {
  var newGlass = new Glass(imagePath);
  newGlass.attach(element);
  return newGlass;
}
