import PropTypes from 'prop-types';
import { react } from 'react'

class Homepage extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pages: props.pages
    };
  }

  componentDidMount() {
    
  }

  render() {
    const { pages } = this.state;
    return (
      <div>
      </div>
    );
  }
}

Homepage.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
  pages: PropTypes.instanceOf(Array)
};

Homepage.defaultProps = {
  // default prop values go here if not required
  pages: []
};

render(
    <div>
      <Homepage />
    </div>,
    document.getElementById('reactEntry'),
  );