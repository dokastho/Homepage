import PropTypes from 'prop-types';
import React from 'react'

class Scroller extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastFired: 0,
      scrollSum: 0,
      coolDown: 1000,
      thresh: 200,
    };
    window.addEventListener("wheel", (event) => {
      const timestamp = event.timeStamp;
      const { lastFired, coolDown } = this.state;
      if (timestamp - lastFired < coolDown) {
        return;
      }
      event.preventDefault();
      event.stopPropagation();

      const { scrollSum, thresh } = this.state;
      const currentScrollPosition = event.wheelDeltaY;
      const { onScroll } = this.props;

      const updatedScrollSum = scrollSum + currentScrollPosition;
      const delta = Math.abs(updatedScrollSum)

      if (delta > thresh) {
        if (0 < updatedScrollSum) {
          onScroll("up");
        } else if (updatedScrollSum < 0) {
          onScroll("down");
        }

        this.setState({
          lastFired: timestamp,
          scrollSum: 0,
        });
      } else {
        this.setState({
          scrollSum: updatedScrollSum,
        })
      }
    })
  }

  render() {
    const { scrollSum } = this.state;
    const c = '.';
    const pbstr = c.repeat(Math.abs(scrollSum / 4));
    return(
      <div>{pbstr}</div>
    );
  }
}



Scroller.propTypes = {
  // prop types go here
  // onScroll
};

export default Scroller
