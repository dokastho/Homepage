import PropTypes from 'prop-types';
import React from 'react';

class Scroller extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastFired: 0,
      scrollSum: 0,
      coolDown: 250,
      thresh: 1000,
    };
  }

  componentDidMount() {
    window.addEventListener("wheel", this.handleScroll);
    this.setState({ lastFired: Date.now() });
  }

  componentWillUnmount() {
    window.removeEventListener("wheel", this.handleScroll);
  }

  handleScroll = (event) => {
    const timestamp = Date.now();
    const { lastFired, coolDown } = this.state;
    if (timestamp - lastFired < coolDown) {
      return;
    }
    const { scrollSum, thresh } = this.state;
    const { onScroll } = this.props;
    const currentScrollPosition = event.wheelDeltaY;

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
  }

  render() {
    const { scrollSum, thresh } = this.state;
    const frac = 100 * scrollSum / thresh;
    return (
      <svg clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" width="4vh" height="4vh" xmlns="http://www.w3.org/2000/svg"><path d="m9.001 13.022h-3.251c-.412 0-.75.335-.75.752 0 .188.071.375.206.518 1.685 1.775 4.692 4.945 6.069 6.396.189.2.452.312.725.312.274 0 .536-.112.725-.312 1.377-1.451 4.385-4.621 6.068-6.396.136-.143.207-.33.207-.518 0-.417-.337-.752-.75-.752h-3.251v-9.02c0-.531-.47-1.002-1-1.002h-3.998c-.53 0-1 .471-1 1.002z" fill-rule="nonzero"/></svg>
    );
  }
}



Scroller.propTypes = {
  // prop types go here
  // onScroll
  pageNum: PropTypes.number.isRequired
};

export default Scroller
