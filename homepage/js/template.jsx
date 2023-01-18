import PropTypes from 'prop-types';
import React from 'react'

class T extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      // a: props.a
    };
  }

  componentDidMount() {
    const {} = this.props;

    this.setState({});
  }

  render() {
    const { } = this.state;
    return (
      <div>
      </div>
    );
  }
}

T.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
};

T.defaultProps = {
  // default prop values go here if not required
};

export default T

// OR

render(
  <div>
    <T />
  </div>,
  document.getElementById('reactEntry'),
);
