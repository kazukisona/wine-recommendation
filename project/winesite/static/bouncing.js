

function Bounce() {
   return React.createElement(
      "div",
      null,
      React.createElement(
         "h1",
         { className: "animated shake  delay-2s" },
         "Find your perfect wine today "
      )
   );
}

ReactDOM.render(React.createElement(Bounce, null), document.querySelector('.bounceHeader'));