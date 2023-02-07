import PropTypes from 'prop-types';
import React from 'react'

class Page extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      title: props.title,
      description: props.description,
      body: props.body,
      route: props.route,
    };
  }

  render() {
    const {
      title,
      description,
      body,
      route,
    } = this.state;
    return (
      <div className={"center-stage-page"}>
        <div className="item-card-content">
          <h1>{title}</h1>
          <h4>{description}</h4>
          <h4>{body}</h4>
          <h4>{route}</h4>
        </div>
      </div>
    );
  }
}

Page.propTypes = {
  // prop types go here
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
};

Page.defaultProps = {
  // default prop values go here if not required
  body: "",
  route: "",
};

export default Page
