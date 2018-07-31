

function NavBar() {
  return React.createElement(
    "div",
    null,
    React.createElement(
      "div",
      { className: "container" },
      React.createElement(
        "div",
        { className: "navbar-header" },
        React.createElement(
          "button",
          { type: "button", className: "navbar-toggle collapsed", "data-toggle": "collapse", "data-target": "#demo-navBar", "aria-expanded": "false" },
          React.createElement(
            "span",
            { className: "sr-only" },
            "Toggle navigation"
          ),
          React.createElement("span", { className: "icon-bar" }),
          React.createElement("span", { className: "icon-bar" }),
          React.createElement("span", { className: "icon-bar" })
        ),
        React.createElement(
         "a",
          { href: "index.html", className: "navbar-brand" },
          " ",
          React.createElement("i", { className: " fas fa-wine-glass" }),
          "  Wine Selector"
        )
      ),
      React.createElement(
        "div",
        { className: "collapse navbar-collapse", id: "demo-navBar" },
        React.createElement(
          "ul",
          { className: "nav navbar-nav navbar-right" },
          React.createElement(
            "li",
            null,
            " ",
            React.createElement(
              "a",
              { href: "signUp.html" },
              " Sign up "
            )
          ),
          React.createElement(
            "li",
            null,
            " ",
            React.createElement(
              "a",
              { href: "login.html" },
              "  Login    "
            )
          )
        )
      )
    )
  );
}

ReactDOM.render(React.createElement(NavBar, null), document.querySelector('nav'));